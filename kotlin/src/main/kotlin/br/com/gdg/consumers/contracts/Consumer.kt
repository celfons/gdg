package br.com.gdg.consumers.contracts

interface Consumer {

    fun listen(topic: String, key: String, message: String)

}
