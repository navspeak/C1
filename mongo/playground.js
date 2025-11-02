// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
use("practicedb");

let practicedb = db.getCollection("bankdata");
let mid = practicedb.countDocuments() / 2
console.log(mid)

practicedb.find()
    .sort({
        "age": 1
    }).skip(mid).limit(1)

practicedb.find({
    "Date": { $regex: /Feb/ }
})
practicedb.find(
    {
        $and: [
            { "marital": { $in: ["single", "divorced"] } },
            { "contact": { $in: ["cellular", "telephone"] } }
        ]

    }
).sort(
    { "balance": -1 }
).limit(1)


