

const tf = require('@tensorflow/tfjs')
fs = require('fs');


var z = tf.randomNormal([1, 256]);

z.data()
    .then((data) => {
        let out = "";
        data.map((val)=>{out += val + ","} )
        name = "sample_1.txt";
        fs.writeFile(name, out, 'ascii', () => 
            {
                console.log("file written");
            });
    })
z = tf.randomNormal([1, 256]);

z.data()
    .then((data) => {
        let out = "";
        data.map((val)=>{out += val + ","} )
        name = "sample_2.txt";
        fs.writeFile(name, out, 'ascii', () => 
            {
                console.log("file written");
            });
    })
z = tf.randomNormal([1, 256]);

z.data()
    .then((data) => {
        let out = "";
        data.map((val)=>{out += val + ","} )
        name = "sample_3.txt";
        fs.writeFile(name, out, 'ascii', () => 
            {
                console.log("file written");
            });
    })
z = tf.randomNormal([1, 256]);

z.data()
    .then((data) => {
        let out = "";
        data.map((val)=>{out += val + ","} )
        name = "sample_4.txt";
        fs.writeFile(name, out, 'ascii', () => 
            {
                console.log("file written");
            });
    }) 
z = tf.randomNormal([1, 256]);

z.data()
    .then((data) => {
        let out = "";
        data.map((val)=>{out += val + ","} )
        name = "sample_5.txt";
        fs.writeFile(name, out, 'ascii', () => 
            {
                console.log("file written");
            });
    })
