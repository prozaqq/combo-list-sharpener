# combo-list-sharpener
A Simple tool to sharpen a combolist according specific password rules .

This script will take a combo list of usernames and passwords delimited by " : " 
and will output a sharpened combolist to a new file according to your specific password rules.

```
usage : sharpener.py -f <filename>
```

<b>Additional flags :</b>

```
[-f] [--file-path] - filepath to the list .
[-ol] [--only-letters] - Password rules allows only letters password ?  # Type true / false or yes / no
[-on] [--only-numbers] - Password rules allows only numbers password ?  # Type true / false or yes / no
[-sc] [--special-chars] - Password rules requires special characters ?  # Type true / false or yes / no
[-cl] [--capital-letters] - Password rules requires a capital letter ?  # Type true / false or yes / no
[-min] [--min-chars] - Set minimum password length .
[-max] [--max-chars] - Set maximum password length .

```
