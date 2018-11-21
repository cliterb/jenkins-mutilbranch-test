#!groovy
node {
    properties ([parameters([string(defaultValue: '', description: '请输入要发布的版本', name:'VERSION')])])
    if (params.VERSION == '') {
        error '参数输入不能为空'
    }
    
    stage('Build'){
        /*拉取当前分支的内容*/
        checkout scm
        def customImage = docker.build("$Docker_registry/$Docker_project/k8sdeamon:${params.VERSION}")
        
        /* Docker Registry */
        docker.withRegistry('https://$Docker_registry', 'registrycredentials-id') {
            /* Push the container to the harbor */
            customImage.push()
            customImage.push('latest')
        }
    }
}
