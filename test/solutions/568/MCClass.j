.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_3
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	dup
	iconst_2
	iconst_1
	bastore
	putstatic MCClass/x [Z
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	iconst_3
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	dup
	iconst_2
	iconst_0
	bastore
	putstatic MCClass/x [Z
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label2:
	getstatic MCClass/x [Z
	iload_1
	getstatic MCClass/x [Z
	iload_1
	baload
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	iconst_1
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	bastore
Label3:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label4
Label5:
	iconst_0
	istore_1
Label14:
	iload_1
	iconst_3
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label15
Label12:
	getstatic MCClass/x [Z
	iload_1
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label13:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label14
Label15:
Label1:
	return
.limit stack 24
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
