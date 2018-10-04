FROM openjdk:8-jdk-alpine
VOLUME /tmp
ADD target/kotlin-1.0-SNAPSHOT.jar app.jar
ENTRYPOINT ["java","-jar","-Dspring.profiles.active=local","app.jar"]
