
../../../bin/xsb -e "[xsbpy],init_xsbpy:test_xsbpy,halt. " >& /dev/null

grep '!!!' test_xsbpy_out.txt

status=0
diff -w  test_xsbpy_out.txt test_xsbpy_out_old || status=1
if test "$status" = 0 ; then 
	echo "xsbpy successfuly tested"
	rm -f test_xsbpy_out.txt
else
	echo "xsbpy test failed: test_xsbpy_outs differ!!!"
	diff -w  test_xsbpy_out.txt test_xsbpy_out_old
fi

