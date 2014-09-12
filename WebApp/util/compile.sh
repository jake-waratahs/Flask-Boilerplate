# lessc --clean-css -x StickiSkinz/static/css/base.less > StickiSkinz/static/css/base.min.css

# lessc --clean-css -x StickiSkinz/static/css/pages/categories.less > StickiSkinz/static/css/base.min.css



# lessc --clean-css -x StickiSkinz/static/js/vendor/typeahead/typeahead.less > StickiSkinz/static/js/vendor/typeahead/typeahead.min.css
echo " * Compiling Less"

files=`find $1 -name '*.less' | cat`
for file in $files
do
	# echo "------------------"
	# echo "Compiling: $file"
	echo "   - Compiling: $file"
	basename=`echo $file | sed s/[\.\\\/A-Za-z0-9\-]*\\\///g`
	basename=`echo $basename | sed s/.less//g`


	basepath=`echo $file | sed s/\\\/[A-Za-z0-9\.\-]*\.less$//`
	basepath=`echo $basepath/`
	# echo $basepath
	# echo $basename
	lessc --clean-css -x "$file" > "$basepath/$basename.min.css"
	# echo "\n"
done

echo " * Less compilation complete."