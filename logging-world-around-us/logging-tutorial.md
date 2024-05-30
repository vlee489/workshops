# Storing data to use

## Introduction @showdialog
In this first part of this workshop we'll walk through all the different sensors the micro:bit has and we'll build the code on storing the data so that we can have a look at it later.

## {Step 1 @showhint}
Click on ``||datalogger: Data Logger||`` category in the Toolbox.
Drag the ``||datalogger: log data||`` block into the ``||loops: every 1000 ms||`` block.

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
Drag the ``||input: temperature (°C)||`` block into the the block box next to ``||datalogger: value||``
Finally we need to give set the name of what this will be stored as, in the field next to  ``||datalogger: column||`` set this to `"temperature"`


```diffblocks
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("", 0),
    )
})
----------
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("temperature", input.temperature()),
    )
})
```

## {Step 4}
Now the next item we're going to add is the ``||input: compass heading (°)||``

To begin, click the `+` button on the ``||datalogger: Data Logger||`` block you already have out. Then head to ``||datalogger: Data Logger||`` and drag a ``||datalogger: column "" value 0||`` into slot that appeared when you pressed the `+` button

Then head over to ``||input: Input||`` category in the Toolbox.
Drag the ``||input: Compass Heading (°C)||`` block into the the block box next to ``||data: value||``
Finally we need to give set the name of what this will be stored as, in the field next to  ``||datalogger: column||`` set this to `"heading"`

```diffblocks
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("temperature", input.temperature()),
    )
})
----------
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("temperature", input.temperature()),
    datalogger.createCV("heading", input.compassHeading())
    )
})
```

## {Step 5}
Now the next item we're going to add is the ``||input: light level||``

First of all, click the `+` button on the ``||datalogger: Data Logger||`` block you already have out. Then head to ``||datalogger: Data Logger||`` and drag a ``||datalogger: column "" value 0||`` into slot that appeared when you pressed the `+` button

Then head over to ``||input: Input||`` category in the Toolbox.
Drag the ``||input: light level||`` block into the the block box next to ``||data: value||``
Finally we need to give set the name of what this will be stored as, in the field next to  ``||datalogger: column||`` set this to `"light"`

```diffblocks
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("temperature", input.temperature()),
    datalogger.createCV("heading", input.compassHeading())
    )
})
----------
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("temperature", input.temperature()),
    datalogger.createCV("heading", input.compassHeading()),
    datalogger.createCV("light", input.lightLevel())
    )
})
```

## {Step 6}
Finally the next item we're going to add is the ``||input: acceleration||``

First of all, click the `+` button on the ``||datalogger: Data Logger||`` block you already have out. Then head to ``||datalogger: Data Logger||`` and drag a ``||datalogger: column "" value 0||`` into slot that appeared when you pressed the `+` button

Then head over to ``||input: Input||`` category in the Toolbox.
Drag the ``||input: acceleration||`` block into the the block box next to ``||data: value||``
Finally we need to give set the name of what this will be stored as, in the field next to  ``||datalogger: column||`` set this to `"acceleration"`

```diffblocks
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("temperature", input.temperature()),
    datalogger.createCV("heading", input.compassHeading())
    )
})
----------
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("temperature", input.temperature()),
    datalogger.createCV("heading", input.compassHeading()),
    datalogger.createCV("light", input.lightLevel()),
    datalogger.createCV("acceleration", input.acceleration(Dimension.X))
    )
})

```

## {Step 7}
Now you should have completed the code to load onto your micro:bit, go and use the download button to uplaod the code onto your micro:bit and move over to the next activity.

```blocks
loops.everyInterval(1000, function () {
    datalogger.log(
    datalogger.createCV("temperature", input.temperature()),
    datalogger.createCV("heading", input.compassHeading()),
    datalogger.createCV("light", input.lightLevel()),
    datalogger.createCV("acceleration", input.acceleration(Dimension.X))
    )
})
```


```template
loops.everyInterval(1000, function () {})
```

```package
datalogger
```