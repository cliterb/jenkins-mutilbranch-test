#!groovy
node {
    properties ([parameters([string(defaultValue: '', description: '请输入要发布的代码标签', name: 'GIT_TAG'),string(defaultValue: '', description: '请输入要发布的版本', name:'VERSION'), string(defaultValue: '', description: '请输入更新内容', name:'RELEASE_NOTE')])])
    if (params.GIT_TAG == '' || params.VERSION == '') {
        error '参数输入错误'
    }
}
