package br.com.gdg.consumers

interface Consumer {

    fun listen(topic: String, key: String, message: String)

}
