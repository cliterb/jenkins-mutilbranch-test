#!groovy
node {
    sh 'rm -rf *'
    sh 'git clone https://github.com/cliterb/mutilbranch-test.git'
    sh 'cd mutilbranch-test && git checkout origin/b1'
    sh 'cd mutilbranch-test && sudo docker build -t $Docker_registry/$Docker_project:$BUILD_TAG  .'
}
