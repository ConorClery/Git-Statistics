const express = require('express');
const fetch = require('node-fetch');
const firebase = require('firebase');
const config = require('../config.json');
// Initialize Firebase
// Initialize Firebase
var firebaseConfig = {
  apiKey:config.apiKey,
  authDomain: config.authDomain,
  databaseURL: config.databaseURL,
  projectId: config.projectId,
  storageBucket: config.projectId,
  messagingSenderId: config.messagingSenderId
};
firebase.initializeApp(firebaseConfig);


const router = express.Router();

router.get('/', function(req, res) {

    console.log('===================================================================' +
        '\nRetrieving home page...\n');
    //API to fetch stuff from Database/backend, encode json in {}
    var db = firebase.database();
    var ref = db.ref("languageData/-LRMQGAS0Uyg2hDf6W1H");

    // Attach an asynchronous callback to read the data at our posts reference
    ref.on("value", function(snapshot) {
      const data = snapshot.val();
      res.render('../public/page/home', {"moop":"moop",
                                         "languageData": data});
    }, function (errorObject) {
      console.log("The read failed: " + errorObject.code);
      res.render('../public/page/home');
    });
});

module.exports = router;
