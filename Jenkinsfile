#!groovy
node {
    properties ([parameters([string(defaultValue: '', description: '请输入要发布的版本', name:'VERSION')])])
    if (params.VERSION == '') {
        error '参数输入不能为空'
    }
    
    stage('Build'){
        /*拉取当前分支的内容*/
        checkout scm
        def customImage = docker.build("$Docker_project/k8sdeamon:${params.VERSION}")
        
        /* Docker Registry */
        /*push前会进行docker tag,所以在docker build的时候不要写registry URL*/
        docker.withRegistry('https://$Docker_registry', 'registrycredentials-id') {
            /* Push the container to the harbor */
            customImage.push()
            /*customImage.push('latest')*/
        }
    }
    
    stage('deploy'){
        def imagename = "$Docker_registry/$Docker_project/k8sdeamon:${params.VERSION}"
        sh "sed -i 's!image_name!$imagename!g' deploy.json"
        sh 'curl -X POST -H "Content-type: application/json" -d@deploy.json http://10.12.76.200:8080/v2/apps'
    }
}
