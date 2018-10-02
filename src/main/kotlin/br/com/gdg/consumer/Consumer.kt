package br.com.gdg.consumer

interface Consumer {

    fun listen(topic: String, key: String, message: String)

}
