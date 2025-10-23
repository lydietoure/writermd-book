
# WriterMD: Book Template

*This repository contains a tool for managing book writing projects, forked from the original [book-template](https://avastmist.github.com/book-template/) project by AvastMick.*

:book: The [template directory](wip-templace) contains a generic template for to work on your next writing project.

:keyboard: The writermd tool is a command line utility written in Python that helps you manage and export your book project into various ebook formats.

To write your book, you can either use the template directory directly, or you can use the writermd tool to create a new book project with the necessary structure and files.
Either way, you would be working with Markdown files to write your pages (extension `.md`), and Git to manage your project versions.

Simple.

## Getting started

If you want to use this template, you can simply download the template directory and start from there. You do not need to use the writermd tool until you are ready.

### Using the template

- Add chapters in the `chapters` directory
- Add cover art and save as `images/book-cover.jpg`
- Put all your planning stuff into planning
- Write away...
    + Add a synopsis set into the `synopsis` folder
    + Add chapters into the `chapters` folder
    + Modify the files in the `publish` folder to suit (only relevant if you are using the application; see the files there for guidance, and the [usage section](#usage) below).

Markdown is a very simple, minimal markup language that is very easy to use. The simplest way to work with this project is by using a very simple text editor (even good old Notepad will do!). But there are also some specialised applications for it, including:
- [Visual Studio Code](https://code.visualstudio.com/) with the [Markdown All in One extension](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Obsidian](https://obsidian.md/) is a very elegant editor, with a number of plugins to help you write a great many things. Check out [the longform plugin for Obsidian](https://github.com/kevboh/longform) if you would prefer a graphical interface to manage your book project with Obsidian.
- [Joplin](https://joplinapp.org/) is another great Markdown editor that can help you manage your writing projects.
- [Microsoft.Edit](https://github.com/microsoft/edit) is a terminal-based text editor, if you prefer working in the terminal.
- [QuickEdit](https://quickedit.io/) is a text editor for Android devices, if you want to write on the go.

I prefer Visual Studio Code, since this project is CLI-based, and VS Code has a great terminal built in.

### Using the writermd tool
If you are looking for a more complete solution, then you should download the writermd tool from [the release page]() to get started.

Prerequisites:
- Git installed on your machine. You can install it from [here](https://git-scm.com/). Git is the version control system used to manage your book project. This will enable you to track changes and different versions of your book, as well as collaborate with others if needed.
- A Gitlab or GitHub account to host your book project (optional, but recommended). If you do not want to host, you can just use the tool locally.
- The writermd tool itself.

## Usage

You can begin a new project by running the following command in your terminal, in the directory where you want to create your book project:

```bash
writermd new "Your Book Title"
```

This will create a new directory called `your-book-title` (essentially, your title, in lower [kebab-case]()) with the necessary structure and files to start writing your book.
If you want to specify a different directory name, you can use the `--dir` option:

```bash
writermd new "Your Book Title" --dir my-book
```
This will create a directory called `my-book` instead of `your-book-title`.

Importantly, the directory will contain a `writermd.yml` configuration file, which you can edit to customize your book project settings. If you remove it, the tool will not work and it will not known what to do!

By default, the tool will create a Git repository for your book project. It will also expect your actual book content to be in the `chapters` directory. You can change these settings in the `writermd.yml` file, or specify them using the `--source` option when creating a new project. For example, to specify that the source files are in a directory called `sections`, you can run:

```bash
writermd new "Your Book Title" --source sections
```

If you somehow lose the `writermd.yml` file, you would need to re-initialize a project in the existing directory using using the `--init`, and optionally `--source` to specify the source directory:

```bash
writermd new "Your Book Title" --init --source pages
```

This will create a new `writermd.yml` file in the current directory without creating a new directory.

## Exporting your book

You can export your book into various formats using the `export` command. The supported formats are:
- EPUB
- DOCX
- PDF
- HTML
- MOBI

To export your book, navigate to your book project directory and run the following command:

```bash
writermd export --format epub
```
The `--rename` option can be used to specify a custom name for the output file. By default, the output file will be named after your book title, with the date prefixed. For example, if your book title is "My Book" and you export it on January 1, 2023, the output file will be named `20230101-my-book.epub` in the `drafts` directory


## Configuration

The `writermd.yml` file contains various settings that you can customize for your book project. Here are some of the key settings:



## How to use

The template uses a couple of libraries:

- [Pandoc](http://pandoc.org)
- [Kindlegen](https://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000765211)

Install those first.

Then clone this repo to your machine. `git clone https://github.com/avastmick/book-template.git`

:boom: Boom, you're done!



## Use locally

### Dependences

- Install python (should be good to go on Linux or MacOS)
- Install [Pandoc](http://pandoc.org)
- Install [Kindlegen](https://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000765211) and ensure you can get to it from your `$PATH`

### Usage
- Open a terminal
- cd to the directory you are saving your book
- type `./Publish.py -h` (MacOS or Linux) or `python Publish.py -h` (Windows) and follow the instructions

## Using Gitlab

I use [Gitlab](http://gitlab.com), why? It has free private repositories, you want that if you are writing a novel, right? Also, it has a free `continuous integration` feature called Pipeline, this can be configured to create your ebooks each time you save you work.

- Commit your changes and push up to [Gitlab](http://gitlab.com)
- Set up a pipeline for building your
- Check the pipeline for success
- Download the build artefacts
- Read...

## Using GitHub

GitHub is great if you are writing open source books etc. It has more users and a greater potential readership.

I'll post up some information on how this template will work.
