
# Prompting

> [Reference](https://learnprompting.org/docs/basics/prompt_engineering)


## Add instructions

If the prompt is too vage, redefine the prompt by encouraging a step-by-step reasoning, that means, add at the end of the prompt any of the following lines (or similar):
1. *let's think step by step*
1. *break it down into smaller steps*
1. *highlight `[required information/data]`*, *with `[required information/data]`*, *include `[required information/data]`*
1. *[example of the expected output] give me a similar description*


## Role prompt

Specify a description of the role AI is going to take to create the output in a specific language. This description is mostly put at the beginning of the prompt:
1. *you are a `[role]` `[some details of the role]` `[prompt content]`*


## Shot prompting

| | |
| --- | --- |
| Zero-shot | Single prompt |
| One-shot | Single prompt plus an example* |
| Few-shot | Single prompt plus few examples* |

> \* Any inspiration/layout of how the output is expected
