#!/bin/bash
fswatch -0 . | while read -d "" event
do
    # Handle file change events and reload appropriate services
    case "$event" in
        *.scss)
            echo "SCSS changesd";
            make build_css;
            ;;
        *.js)
            echo "JS changed";
            ;;
        *.py)
            echo "Python changed";
            ;;
        *.html)
            echo "HTML change";
            ;;
        *)
            echo "No handler for file type."
            ;;
    esac
done
