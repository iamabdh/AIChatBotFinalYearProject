// Load config
const dotenv = require("dotenv");
dotenv.config({ path: "./config/.env" });
require("./models/connectMongoDB")
const IntentSchema = require("./models/intentSchema")
const fs = require("fs")
const res = fs.readFileSync("./config/intents.json", "utf-8");
let parsedRes = JSON.parse(res)

parsedRes.intents.forEach((intent) => {
   new IntentSchema({
       tag : intent.tag,
       pattern: intent.patterns,
       flag: intent.flag,
       response: intent.response,
       context: intent.context_set,
       init: intent.init,
       required: intent.required
   }).save()
       .then(res=> console.log(res)).catch(err => console.log(err))
})
