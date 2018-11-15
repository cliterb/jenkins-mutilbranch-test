#!groovy 
// -*- mode: groovy -*- 
node { 
    sh 'env > env.txt' 
    sh 'echo hello, this is b1' 
    readFile('env.txt').split("\r?\n").each { 
        println it 
    } 
} 
