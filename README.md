# paperpileConvert
Converts PaperPile JSON data into YAML suitable for Jekyll websites

## Installation

```
pip install git+git://github.com/scrim-network/paperpileConvert.git#egg=paperpileConvert
```

## Usage

```
from paperpileConvert import *
convert(['tag1', 'tag2', ..., 'tagN'], filename, path=your_output_directory)
```

## Details

[PaperPile](https://paperpile.com/welcome) is a convenient way to store and share your research library. However, options are limited when exporting references for use on other applications or mediums. The options as of this writing are plain text, BibTeX, RIS, and CSV. None of these formats are convenient for website publishing.

PaperPile does offer a database export as a JSON file as well. This module uses Python to parse and convert the JSON export into YAML format. The format is specifically designed to work with [Jekyll](https://jekyllrb.com/) websites.

The conversion begins in PaperPile. Publications must be tagged within the PaperPile database. Simply tag all of the publications you wish to convert prior to exporting the database. Multiple tags can be exported at once. Then, export the database under "Settings -> Export."

Next, follow usage convention above. Specify all of the tags your wish to have converted. The output directory can be specified, but the current working directory will be used if it's not.

The module will create 1 page for each tag named ```<tag name>.md```, which contains the data for all references with that tag, and 1 folder (```<tag name>```) that will have 1 page for each individual reference.

Because the data is in YAML format, Jekyll's templating software "Liquid" can be used to display the data. For help with this, see [JekyllBib](https://github.com/scrim-network/JekyllBib).
