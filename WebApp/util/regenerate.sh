echo " * Regenerating $2s"

rm -rf $1/__init__.py

for directory in $1/*/
do
   if [ -f "${directory}__init__.py" ] 
   then
      basename=`basename "$directory"`
      echo "   - Found Submodule: $basename"
      echo "from $basename import $basename" >> $1/__init__.py
   fi

done

for file in $1/*.py
do
   basename=`basename "$file"`
   basename=`echo "$basename" | sed 's/\.py//'`
   if [ $basename != "__init__" ]
   then

      echo "   - Found Module: $basename"
      echo "from $basename import $basename" >> $1/__init__.py
   fi
done
echo " * $2 Regeneration Complete"

