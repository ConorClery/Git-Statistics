const express = require('express');
const fetch = require('node-fetch');
const router = express.Router();

router.get('/', function(req, res) {

    console.log('===================================================================' +
        '\nRetrieving home page...\n');
    //API to fetch stuff from Database/backend, encode json in {}
    res.render('../public/page/home', {});

});

module.exports = router;
