.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static sort([I)[I
.var 0 is arr [I from Label0 to Label1
.var 1 is i I from Label0 to Label1
	bipush 50
	istore_1
Label0:
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_5
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
.var 2 is j I from Label2 to Label3
	iconst_3
	istore_2
Label2:
	iload_1
	iconst_1
	iadd
	istore_2
Label10:
	iload_2
	iconst_5
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
Label8:
	getstatic MCClass/arr [I
	iload_1
	iaload
	getstatic MCClass/arr [I
	iload_2
	iaload
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label14
.var 3 is temp I from Label18 to Label19
	iconst_0
	istore_3
Label18:
	getstatic MCClass/arr [I
	iload_1
	iaload
	istore_3
	getstatic MCClass/arr [I
	iload_1
	getstatic MCClass/arr [I
	iload_2
	iaload
	iastore
	getstatic MCClass/arr [I
	iload_2
	iload_3
	iastore
Label19:
	goto Label15
Label14:
Label20:
Label21:
Label15:
Label9:
	iconst_1
	iload_2
	iadd
	istore_2
	goto Label10
Label11:
Label3:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label4
Label5:
	getstatic MCClass/arr [I
	areturn
Label1:
	return
.limit stack 17
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 7
	iastore
	dup
	iconst_2
	iconst_1
	iastore
	dup
	iconst_3
	iconst_2
	iastore
	dup
	iconst_4
	bipush 6
	iastore
	putstatic MCClass/arr [I
.var 1 is i I from Label0 to Label1
	bipush 100
	istore_1
Label0:
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_5
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label2:
	getstatic MCClass/arr [I
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label3:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label4
Label5:
	invokestatic io/printLn()V
	getstatic MCClass/arr [I
	invokestatic MCClass/sort([I)[I
	putstatic MCClass/arr [I
	iconst_0
	istore_1
Label10:
	iload_1
	iconst_5
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
Label8:
	getstatic MCClass/arr [I
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label9:
	iconst_1
	iload_1
	iadd
	istore_1
	goto Label10
Label11:
Label1:
	return
.limit stack 18
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
