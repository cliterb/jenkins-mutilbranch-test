#!groovy
node {
    sh 'sudo docker build -t $Docker_registry/$Docker_project:$BUILD_TAG  .'
    sh 'git clone https://github.com/cliterb/mutilbranch-test.git'
}
