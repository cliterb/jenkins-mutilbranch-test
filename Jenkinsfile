#!groovy
node {
    sh 'git clone https://github.com/cliterb/mutilbranch-test.git'
    sh 'cd mutilbranch-test && git checkout origin/master'
    sh 'sudo docker build -t $Docker_registry/$Docker_project:$BUILD_TAG .'
}
