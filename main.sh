#!/bin/bash

case $1 in 
    
    # Show the help message
    -h | --help)
    echo "Options:"
    echo "  -h, --help: Show this help message"
    echo "  run_scrape: Scrape the data from the website"
    echo "  print_scrape: Scrape the data and print it to the terminal"
    echo "  keyword_search: Run a keyword search on user input"
    ;;

    # Run get_data function
    run_scrape)
    python -c'import common.py; common.get_data()'
    
    ;;

    # Run print_df function
    print_scrape)
    python -c'import common.py; common.print_df()'

    ;;

    # Run run_search function
    keyword_search)
    echo "Enter a keyword to search for: "
    read keyword
    python -c'import common.py; common.run_search(keyword)'


    ;;
esac


