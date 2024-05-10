# Storing data to use

## Introduction @showdialog
In this first part of this workshop we'll walk through all the different sensors the micro:bit has and we'll build the code on storing the data so that we can have a look at it later.

## {Step 1 @showhint}
Click on ``||data: Data Logger||`` category in the Toolbox.
Drag the ``||data: log data||`` block into the ``||loops: every 1000 ms||`` block.

```blocks
loops.everyInterval(1000, function () {
    datalogger.log(datalogger.createCV("", 0))
})
```

## {Step 2}
Now that we have the the basic building blocks that will lock 


```template
loops.everyInterval(1000, function () {})
```