const express = require('express');
const fetch = require('node-fetch');
const firebase = require('firebase');
// Initialize Firebase
// Initialize Firebase
var config = {
  apiKey: "AIzaSyDoC0UaSQg6MJ7KHQCFny7hp6TGlk7zEi8",
  authDomain: "swengdb.firebaseapp.com",
  databaseURL: "https://swengdb.firebaseio.com",
  projectId: "swengdb",
  storageBucket: "swengdb.appspot.com",
  messagingSenderId: "766339450185"
};
firebase.initializeApp(config);


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
