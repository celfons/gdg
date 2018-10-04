package br.com.gdg.models

import javax.persistence.Column
import javax.persistence.Entity
import javax.persistence.GeneratedValue
import javax.persistence.GenerationType
import javax.persistence.Id
import javax.persistence.SequenceGenerator
import javax.persistence.Table

@Entity
@Table(name = "message", schema="mydatabase")
data class Message(
        @Id @Column(name="id")
        @SequenceGenerator(name = "SEQ", sequenceName = "message_id_seq")
        @GeneratedValue(strategy= GenerationType.IDENTITY, generator = "SEQ")
        val id: Long? = null,
        @Column(name="name") val name: String? = null,
        @Column(name="msg") val text: String? = null
)
