package br.com.gdg.config

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.EnableAutoConfiguration
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.autoconfigure.domain.EntityScan
import org.springframework.context.annotation.ComponentScan
import org.springframework.data.jpa.repository.config.EnableJpaRepositories

@SpringBootApplication
@EnableAutoConfiguration
@ComponentScan("br.com.gdg")
@EntityScan("br.com.gdg.models")
@EnableJpaRepositories("br.com.gdg.repositories")

open class Gdg

fun main(args: Array<String>) {
    SpringApplication.run(Gdg::class.java, *args)
}
