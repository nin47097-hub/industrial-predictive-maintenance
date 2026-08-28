const express = require("express");

const {
    predictions,
    getMachine,
    getMachines
} = require("../Controllers/predict.Controller");

const router = express.Router();

router.post("/predict", predictions);

router.get("/machines/:machine_id", getMachine);

router.get("/machines", getMachines);

module.exports = router;