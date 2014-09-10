echo " * Regenerating $2s"

rm -rf $1/__init__.py
for file in $1/*.py
do
   basename=`basename "$file"`
   basename=`echo "$basename" | sed 's/\.py//'`
   echo "from $basename import *" >> $1/__init__.py
done
echo " * $2 Regeneration Complete"