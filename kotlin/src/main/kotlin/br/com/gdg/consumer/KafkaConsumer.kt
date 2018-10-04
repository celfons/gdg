package br.com.gdg.consumer

import br.com.gdg.model.Message
import br.com.gdg.repository.MessageRepository
import com.google.gson.Gson
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.kafka.annotation.KafkaListener
import org.springframework.kafka.support.KafkaHeaders
import org.springframework.messaging.handler.annotation.Header
import org.springframework.stereotype.Component

@Component
class KafkaConsumer : Consumer {

    @Autowired private lateinit var messageRepository: MessageRepository

    @KafkaListener(topics = ["mytopic"], groupId = "mygroup")
    override fun listen(
            @Header(KafkaHeaders.RECEIVED_TOPIC) topic: String,
            @Header(KafkaHeaders.RECEIVED_MESSAGE_KEY) key: String, message: String
    ) {
        val messageObject = Gson().fromJson(message, Message::class.java)
        saveMessage(messageObject)
    }

    private fun saveMessage(messageObject: Message?) {
        try {
            messageRepository.save(messageObject)
        } catch (e: Exception) {
            println(e)
        }
    }

}
