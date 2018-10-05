package br.com.gdg.services.contracts

import br.com.gdg.models.Message

interface Service {

    fun save(message: Message)

}
