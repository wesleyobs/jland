# For Java {{compilation_tool}}
#Oficial docker-hub image eclipse-temuriun
{%set runtime_version = 1.8 if java_compatibility == 8 else java_compatibility %}
FROM eclipse-temurin:{{runtime_version}}
RUN mkdir app
{%set jar_path = "build/libs" if compilation_tool == "Gradle" else "target" %}
ADD {{jar_path}}/{{project_name}}-*-final.jar ./app/springApp.jar
EXPOSE ${SERVER_PORT}
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom","-jar","./app/springApp.jar"]