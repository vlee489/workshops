# Storing data to use

## Introduction @showdialog
In this first part of this workshop we'll walk through all the different sensors the micro:bit has and we'll build the code on storing the data so that we can have a look at it later.

## {Step 1 @showhint}
Click on ``||data: Data Logger||`` category in the Toolbox.
Drag the ``||data: log data||`` block into the ``||loops: every 1000 ms||`` block.

```blocks
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("", 0),
    )
})
```

## {Step 2}
Now that we have the the basic building blocks that will log allow us to store the data from the micro:bit we can now start having a look at what things the micro:bit can see.

## {Step 3}
We'll start at looking at ``||input: Temperature||``, this allows the micro:bit to know how warm or cold the space around it is.

Start by going to ``||input: Input||`` category in the Toolbox.
Drag the ``||input: temperature (°C)||`` block into the the block box next to ``||data: value||``
Finally we need to give set the name of what this will be stored as, in the field next to  ``||data: column||`` set this to `"temperature"`


```blocks
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("temperature", input.temperature()),
    )
})
```

## {Step 4}
How the next item we're going to add is the ``||input: compass heading (°)||``

To begin, click the `+` button on the ``||data: Data Logger||`` block you already have out. Then head to ``||data: Data Logger||`` and drag a ``||data: column "" value 0||`` into slot that appeared when you pressed the `+` button

Then head over to ``||input: Input||`` category in the Toolbox.
Drag the ``||input: Compass Heading (°C)||`` block into the the block box next to ``||data: value||``
Finally we need to give set the name of what this will be stored as, in the field next to  ``||data: column||`` set this to `"heading"`

```blocks
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("temperature", input.temperature()),
    datalogger.createCV("heading", input.compassHeading())
    )
})
```


```template
loops.everyInterval(1000, function () {})
```

```package
datalogger
```