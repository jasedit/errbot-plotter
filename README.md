# Plotter

Plugin for [Errbot](https://errbot.io) which provides the ability to consume numerical data and generate plots, posting them to channels.

# Installation

This can be installed by an errbot admin issuing the command `!repos install https://github.com/jasedit/errbot-plotter`

# Usage

Currently, plots are generated using a command of the form:

```
!plot "1,2;3,4" -t "Title" -x "X-axis Label" -y "Y-axis Label"
```

Where the first sequence of comma-separated numbers are the x values, and the second sequence of comma-separated numbers make up the y values.