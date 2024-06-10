def handle_toggle_menu(main_window, isChecked):
    main_window.widget_sideExpanded.setHidden(isChecked)
    main_window.widget_sideShrinked.setVisible(isChecked)
