node {
     environment {
        registry = "karimnasri/hello_world"
        helloWorldImage = ''
        success = None
     }
    stage('SCM Checkout') {
    git ''
    }

    stage('Build Docker image') {
            steps{
                echo 'Building the docker image ...'
            script {

                    helloWorldImage = docker.build(registry + ${env.BUILD_ID})
                    helloWorldImage.push()
                }
            }
    }
    stage('unittest') {
    steps{
        def testimage = docker.build(registry + ${env.BUILD_ID})
        sh "docker run $registry${env.BUILD_ID} '-m' 'unittest' 'test_hello_world.py' "

    }
    post {
            success{
            echo "Unit tests success"
            ENV.success = True
            }
            failure {
            echo "Failed unit tests"
            ENV.success = False
            }
        }
    }
    if (ENV.success == True) {
    stage('Deploy')  {
        echo "stage deploy"
    }
    }
}