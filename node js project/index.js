const express = require("express")
const app = express()
app.get("/hello", (req,res) => {
    res.send("hello");

});


app.get("/numbers",(req,res)=>{
    let numbers= " ";
    for(let i=0;i<=5;i++){
        numbers+=i + " / ";

    }
    res.send('the numbers are:' + numbers);
});

app.get("/findSummation/:number1/:number2", (req,res)=>{
    const num1 = req.params.number1;
    const num2 = req.params.number2;
    const total = Number(num1)+Number(num2);
    //console.log(req.params);
    //res.send("the numbers are: "+num1+" and "+num2);
    res.send("the total is : "+total);
    
    //console.log("the total is " + total);
})
app.put("/test", (req,res)=>{
    res.send("you visited test");
});
app.post("/addComment",(req,res)=>{
    res.send("post request on add comment");
});
app.listen(3000, () => {
    console.log("I am listening in port 3000");
});
