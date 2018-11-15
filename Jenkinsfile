#!groovy 
// -*- mode: groovy -*- 
node { 
    sh 'env > env.txt' 
    sh 'echo hello, this is master' 
    readFile('env.txt').split("\r?\n").each { 
        println it 
    } 
} 
