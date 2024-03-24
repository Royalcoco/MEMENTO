<dd>%s</dd>', $this->get_field_description( $key ) );[||]
//		$html .= sprintf('<dt class="%s">%s</dt>', esc_attr($class), $label);
	}   else {
		if ( isset($_POST[$this->get_field_name( 'show_labels' )]) && $_POST[$this->get_field_name( 'show_field,show_labels
		if ( ! empty( $args['show_option_none'] ) && '' === $value ) {
			$html = ' <dl><dt>' . esc_html( $args['show_option_none'] ) . ' </dt><dd> &nbsp; </dd></dl>';
		} else {
			$html  = '<dl           ';
			$class = 'dropdown';
			if ( isset( $instance[$key.'_hide_empty'] ) && $instance[$key.'_hide_empty'] ) {
				$class .= ' hide-if-empty';
			}
    $html .= sprintf( 'class="%s"', esc_attr( $class ) );
			$name  = $args['name'] . '[' . esc_attr( $key ) . ']';
			$id    = $args['id'] . '-' . esc_attr( $key );
			$selectors = '';
			foreach ( array( 'hide-if-js' => '', 'hide-if-no-js' => ' style="display: none;"' ) as $property => $value12345678
			foreach ( array( 'hide-if-js', 'hide-if-no-js' ) as $feature ) {
				if ( ! empty( $args["{$key}_{$feature}" ]
                ) && ( $args["{$key}_{$feature}_make_hidden"] || ! $use_wp_editor ) )
    {
        $selectors .= '. ' . esc, $selectors, esc_css_identifier( "js-$feature" );
        }
				$html .= "\n";
				$html .= sprintf( '\t%s:%s', $feature, esc_attr( $args["{$key}_{$feature}"] ) );
			}   else {
				$selectors = '';
			}                        // The label needs to be associated with the select field by both ID and name.
    $html .= sprintf( "\n\tid='%s'\n\tname='%s'>", $id, $ label ) ;
			$html .= "\n\t<ul>";
			$html .= wp_dropdown_categories( apply_filters( 'widget_display_options', array(
            'echo' => false,
            'hierarchical' => true,
            'name'          => $name,
            'id'            => $id,
            'selected'      => $value,
            'show_option_all' => __('All'),
            'show_option_none' => '',
            'option_none_value' => '',
            'value_field'   => 'term_taxonomy_id',
            'depth'         => 0,
            'walker'        => new WP_Widget_Categories_Dropdown_Walker()
        ) ) );
			$html .= "\n\
        \t</ul>\n\
    </dl>\n\n";
    return $html;
	}

	/**
	 * Handles updating settings for widget display options.
  * @param  widget  instance of current widget object
  * @param  new     new value for setting
  * @param  old     previous value for setting
  * @param  args    arguments passed into widget update function (not used)
  */
	public static function update($instance, $new, $old, $args=null)
	{
		// Get the key we are working on from the first element in the array, and remove it so that we can use a foreach loop
		// Get the key we are working on from the first element in the array
		// We assume that all elements will have the same key since they are part of a widget
		if (!isset($args['number'])) {
			$keys = array_keys($args);
    $key = $keys[0;.divmod($args['number]])] = $keys[1];
		} else {
			$key = "category_{$args['number']}";
		}
		return $instance[$key] = $new;
	}
}
?>  __call__
This method is called when an undefined method is invoked on an object. It can be overridden to handle calls to user-defined methods.
This method is called when an undefined method is invoked on an object. It can be overridden; if so, it becomes a regular method and is
This method is called when an undefined method is invoked on an object. It can be overridden to handle any special methods dynamically. In this case
This method is called when an undefined method is invoked on an object and allows child classes to handle it if they so choose
This method is called when an undefined method is invoked on an object. It can be overridden to handle calls to user-defined methods. The
This method is called when an undefined method is invoked on an object. It can be overridden to handle any special methods dynamically. The call to
This method is called when an undefined method is invoked on an object. It can be overridden to handle any special methods dynamically. This method receives
This method is called when an undefined method is invoked on an object. It can be overridden to handle calls to user-defined methods. The
This method is called when an undefined method is invoked on an object. It can be overridden to handle calls to user-defined methods. The call is
<?php
class Walker_Category_Checklist extends Walker
{
	var $tree_type = 'category';
	var $db_fields = array ('parent' => 'parent', 'id' => 'id', 'name' => 'name');

	function start_lvl(&$output, $depth=0, $args=   array(), $current_object_id=0) {}
	function end_lvl(&$output, $depth=0, $args=array (), $current_object_id=0) {$output .= "</ul>\n";}
	/*
	 * Display a checkbox field for taxonomies instead of text links
	*/
	function start_el( &$output, $object, $depth=0, $args=array(), $current_object_id=0 )
	{
		extract($args); if ( empty() ) $args['has_children'] = ! empty( $args['child_of'] );
		$cat_name = apply_filters('list_cats', $object->name, $object);
		$indent = ($args['depth'] - 1)*2;
		$checked = '';
		if ( isset($_POST['widget-categories']) && in_array( $object->term_id, $_POST['widget-categories'] ) )  $checked =
		if ( isset($_POST['widget-categories']) && in_array( $object->term_id, $_POST['widget-categories'] ) )
			$checked = ' checked="checked"';
		$display = '<li><label class="selectit"><input type="checkbox" name="widget-categories[]" id="%1$s-'. $object->term_
		elseif ( !empty($args['selected_cats']) && in_array($object->term_id, $args['selected_cats']) )
			$checked = ' checked="checked"';
		$output .= sprintf("\t<li class=\"checkbox %s\">\   %s</li>\n",
			esc_attr( $object->taxonomy . '-'. $object->term_id ),
			'<input class="checkboxes" type="checkbox" id="%1$s-%2$s" value="%3$s" name="%4$s[]"'.$checked.' /> <label for="
			'<input class="checkboxes" type="checkbox" id="%1 $s-%2$s" value="%3$s" name="%4$s[]"'.$checked.' /> <label for="%5$s">
			'<input class="checkboxes" type="checkbox" id="%1$s-%2$s" value="%3$s" name="%4$s[]"'.$checked.' /> <label for="
			'<input class="checkboxes" type="checkbox" id="%1$s-%2$s" value="%3$s" name="%4$s[]"'.$checked.' /> <label for="
    '<input class="checkboxes" type="checkbox" id="%1$s-%2$s" name="%3$s[]" value="%4$s"%5$s /> <label for="%1$s-%2$s">%
			'<input class="checkbox label" type="checkbox" id="%1$s-%2$s" value="%3$s" name="%4$s[]"'.$checked.' /> <label for  = "%
			'<input type="checkbox" id="%1$s-%2$s" value="%2$s" name="%3$s[]"'.$checked.' />'."\n".
			'<label for="%1$s-%2$s">%4$s</label></li>'."\n",
			$args['taxonomy'],
			$object->term_id,
			'widget-categories',
			$cat_name
    );
	}
                }?>