import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.EnableAutoConfiguration
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.context.annotation.ComponentScan

@SpringBootApplication
@EnableAutoConfiguration
@ComponentScan(
        basePackages = ["br.com.gdg"]
)

open class Gdg

fun main(args: Array<String>) {
    SpringApplication.run(Gdg::class.java, *args)
}
