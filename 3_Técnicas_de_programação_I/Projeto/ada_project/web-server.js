const express = require('express');
const app = express();

const port = process.env.PORT || 3000;

const server = app.listen(port);

server.timeout = 1000 * 60 * 10; // 10 minutes

var init_time = 1578510678;
var time = 1578510678;

const uid = function(){
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
}

function randn_bm() {
    let u = 1 - Math.random(); //Converting [0,1) to (0,1)
    let v = Math.random();
    return Math.sqrt( -2.0 * Math.log( u ) ) * Math.cos( 2.0 * Math.PI * v );
}


// Use middleware to set the default Content-Type
app.use(function (req, res, next) {
    res.header('Content-Type', 'application/json');
    next();
});

app.get('/api/ep1', (req, res) => {
    let array_res = [];
    for (let i = 0; i < Math.floor(Math.random()*200); i++){
        vals = {};
        vals['id'] = uid();
        vals['date'] = time + Math.random()*60000;

        for (let k = 0; k < 10; k++){
            if (Math.random() < 0.5){
                let prod = 'prod_';
                prod += k;
                vals[prod] = Math.random() * 50;
            }
        };

        for (let k = 8; k < 12; k++){
            if (Math.random() < 0.5){
                let prod = 'prod_';
                prod += k; 
                vals[prod] = Math.random() * 800 + Math.cos(2 * Math.PI * (1/(4*604800)) * vals['date']) * 300;
            }
        }

        for (let k = 12; k < 15; k++){
            if (Math.floor() < 0.5){
                let prod = 'prod_';
                prod += k;
                vals[prod] = max(0,randn_bm() * 50);
            }
        };

        if (vals['date'] > 1581189078){
            vals['prod_15'] = Math.random() * 800 + Math.cos(2 * Math.PI * (1/(4*604800)) * vals['date']) * 300 + (vals['date'] - init_time) * 10e-6;
        }

        if (vals['date'] > 1581189078){
            vals['prod_15'] = Math.random() * 800 + Math.cos(2 * Math.PI * (1/(4*604800)) * vals['date']) * 300 + (vals['date'] - init_time) * 10e-6;
        }

        if (vals['date'] > 1604862678){
            vals['prod_15'] = Math.random() * 800 + Math.cos(2 * Math.PI * (1/(24*604800)) * vals['date']) * 500 + (vals['date'] - init_time) * 10e-6;
        }



        array_res.push(vals);
    };

    time += 604800;


    res.send(JSON.stringify(array_res));
})