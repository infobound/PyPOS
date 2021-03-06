#############################################################################
# Generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#  Jul 06, 2020 11:21:39 PM EDT  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top43 {base} {
    global vTcl
    if {$base == ""} {
        set base .top43
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 992x659+428+124
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1908 1045
    wm minsize $top 124 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra44 \
        -borderwidth 2 -relief sunken -background $vTcl(actual_gui_bg) \
        -height 565 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 725 
    vTcl:DefineAlias "$top.fra44" "frameItems" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Patron: 
    vTcl:DefineAlias "$top.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $top.tCo47 \
        -font TkTextFont -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$top.tCo47" "cboPatrons" vTcl:WidgetProc "Toplevel1" 1
    frame $top.fra49 \
        -borderwidth 2 -relief sunken -background $vTcl(actual_gui_bg) \
        -height 485 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 275 
    vTcl:DefineAlias "$top.fra49" "frameOrderItems" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra49
    label $site_3_0.lab50 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief raised -text Item 
    vTcl:DefineAlias "$site_3_0.lab50" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab54 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief raised -text Qty 
    vTcl:DefineAlias "$site_3_0.lab54" "Label2_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab55 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief raised -text {Unit Price} 
    vTcl:DefineAlias "$site_3_0.lab55" "Label2_2" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.007 -y 0 -rely 0.004 -width 0 \
        -relwidth 0.509 -height 0 -relheight 0.049 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 0 -relx 0.513 -y 0 -rely 0.004 -width 0 \
        -relwidth 0.145 -height 0 -relheight 0.049 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.655 -y 0 -rely 0.004 -width 0 \
        -relwidth 0.218 -height 0 -relheight 0.049 -anchor nw \
        -bordermode ignore 
    label $top.lab58 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Sub Total:} 
    vTcl:DefineAlias "$top.lab58" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab59 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify right -text {$000.00} 
    vTcl:DefineAlias "$top.lab59" "lblSubTotal" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab60 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Tax: 
    vTcl:DefineAlias "$top.lab60" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab62 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Total: 
    vTcl:DefineAlias "$top.lab62" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab64 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify right -text {$000.00} 
    vTcl:DefineAlias "$top.lab64" "lblTax" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab65 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {$000.00} 
    vTcl:DefineAlias "$top.lab65" "lblTotal" vTcl:WidgetProc "Toplevel1" 1
    button $top.but67 \
        -activebackground #ff8040 -activeforeground #000000 \
        -background #ff00ff -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Back 
    vTcl:DefineAlias "$top.but67" "btnBack" vTcl:WidgetProc "Toplevel1" 1
    button $top.but69 \
        -activebackground #ff8040 -activeforeground #000000 \
        -background #ff00ff -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Next 
    vTcl:DefineAlias "$top.but69" "btnNext" vTcl:WidgetProc "Toplevel1" 1
    button $top.but70 \
        -activebackground #ff8040 -activeforeground #000000 \
        -background #00ffff -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Credit 
    vTcl:DefineAlias "$top.but70" "btnCredit" vTcl:WidgetProc "Toplevel1" 1
    button $top.but71 \
        -activebackground #ff8040 -activeforeground #000000 \
        -background #00ff00 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Cash 
    vTcl:DefineAlias "$top.but71" "btnCash" vTcl:WidgetProc "Toplevel1" 1
    button $top.but72 \
        -activebackground #ff8040 -activeforeground #000000 \
        -background #ff80c0 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Cancel 
    vTcl:DefineAlias "$top.but72" "btnCancel" vTcl:WidgetProc "Toplevel1" 1
    button $top.but73 \
        -activebackground #ff8040 -activeforeground #000000 \
        -background #ffff80 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Save 
    vTcl:DefineAlias "$top.but73" "btnSave" vTcl:WidgetProc "Toplevel1" 1
    button $top.but44 \
        -activebackground #ff8040 -activeforeground #000000 \
        -background #c0c0c0 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {parent level 1} 
    vTcl:DefineAlias "$top.but44" "btnSave_1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra44 \
        -in $top -x 0 -y 0 -rely 0.061 -width 0 -relwidth 0.731 -height 0 \
        -relheight 0.857 -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 0 -relx 0.736 -y 0 -rely 0.015 -width 0 -relwidth 0.044 \
        -height 0 -relheight 0.032 -anchor nw -bordermode ignore 
    place $top.tCo47 \
        -in $top -x 0 -relx 0.786 -y 0 -width 0 -relwidth 0.213 -height 0 \
        -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.fra49 \
        -in $top -x 0 -relx 0.736 -y 0 -rely 0.061 -width 0 -relwidth 0.277 \
        -height 0 -relheight 0.736 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 0 -relx 0.736 -y 0 -rely 0.804 -width 0 -relwidth 0.059 \
        -height 0 -relheight 0.032 -anchor nw -bordermode ignore 
    place $top.lab59 \
        -in $top -x 0 -relx 0.917 -y 0 -rely 0.804 -width 0 -relwidth 0.065 \
        -height 0 -relheight 0.032 -anchor nw -bordermode ignore 
    place $top.lab60 \
        -in $top -x 0 -relx 0.736 -y 0 -rely 0.835 -width 0 -relwidth 0.034 \
        -height 0 -relheight 0.032 -anchor nw -bordermode ignore 
    place $top.lab62 \
        -in $top -x 0 -relx 0.736 -y 0 -rely 0.865 -width 0 -relwidth 0.066 \
        -height 0 -relheight 0.032 -anchor nw -bordermode ignore 
    place $top.lab64 \
        -in $top -x 0 -relx 0.917 -y 0 -rely 0.835 -width 0 -relwidth 0.066 \
        -height 0 -relheight 0.032 -anchor nw -bordermode ignore 
    place $top.lab65 \
        -in $top -x 0 -relx 0.877 -y 0 -rely 0.865 -width 0 -relwidth 0.108 \
        -height 0 -relheight 0.032 -anchor nw -bordermode ignore 
    place $top.but67 \
        -in $top -x 0 -y 0 -rely 0.926 -width 97 -relwidth 0 -height 44 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.but69 \
        -in $top -x 0 -relx 0.101 -y 0 -rely 0.926 -width 97 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but70 \
        -in $top -x 0 -relx 0.897 -y 0 -rely 0.926 -width 97 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but71 \
        -in $top -x 0 -relx 0.796 -y 0 -rely 0.926 -width 97 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but72 \
        -in $top -x 0 -relx 0.635 -y 0 -rely 0.926 -width 97 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but73 \
        -in $top -x 0 -relx 0.534 -y 0 -rely 0.926 -width 97 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but44 \
        -in $top -x 0 -y 0 -width 97 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top43 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

