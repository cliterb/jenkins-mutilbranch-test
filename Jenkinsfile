#!groovy
node {
    sh 'git fetch https://github.com/cliterb/mutilbranch-test.git b1'
    sh 'sudo docker build -t $Docker_registry/$Docker_project:$BUILD_TAG .'
}
