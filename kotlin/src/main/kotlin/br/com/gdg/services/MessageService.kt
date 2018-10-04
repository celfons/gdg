package br.com.gdg.services

import br.com.gdg.models.Message
import br.com.gdg.repositories.MessageRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Component

@Component
class MessageService : Service {

    @Autowired
    private lateinit var messageRepository: MessageRepository

    override fun save(message: Message) {
       messageRepository.save(message)
    }

}
