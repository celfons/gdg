package br.com.gdg.services

import br.com.gdg.models.Message

interface Service {

    fun save(message: Message)

}
