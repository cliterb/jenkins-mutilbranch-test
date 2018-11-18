#!groovy
node {
    sh 'git clone https://github.com/cliterb/mutilbranch-test.git'
    sh 'git checkout -b master'
    sh 'sudo docker build -t $Docker_registry/$Docker_project:$BUILD_TAG .'
}
