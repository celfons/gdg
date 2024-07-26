package br.com.gdg.consumers

import br.com.gdg.consumers.contracts.Consumer
import br.com.gdg.models.Message
import br.com.gdg.services.MessageService
import com.google.gson.Gson
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.kafka.annotation.KafkaListener
import org.springframework.kafka.support.KafkaHeaders
import org.springframework.messaging.handler.annotation.Header
import org.springframework.stereotype.Component

@Component
class KafkaConsumer : Consumer {

    @Autowired private lateinit var messageService: MessageService

    @KafkaListener(topics = ["\${topic}"], groupId = "\${group}")
    override fun listen(
            @Header(KafkaHeaders.RECEIVED_TOPIC) topic: String,
            @Header(KafkaHeaders.RECEIVED_MESSAGE_KEY) key: String, message: String
    ) {
        val messageObject = Gson().fromJson(message, Message::class.java)
        saveMessage(messageObject)
    }

    
    private fun saveMessage(messageObject: Message) {
        try {
            messageService.save(messageObject)
        } catch (e: Exception) {
            println(e)
        }
    }

}
