#!groovy
node {
    properties ([parameters([string(defaultValue: '', description: '请输入要发布的版本', name:'VERSION')])])
    if (params.VERSION == '') {
        error '参数输入不能为空'
    }
    
    stage('Build'){
        /*拉取当前分支的内容*/
        checkout scm
        def customImage = docker.build("example-group/example:${params.VERSION}")

        /* hub.xxxx.cn是你的Docker Registry */
        docker.withRegistry('https://hub.xxxx.cn/', 'docker-registry') {
            /* Push the container to the custom Registry */
            customImage.push()
            customImage.push('latest')
        }
    }
}
