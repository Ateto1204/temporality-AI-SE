author:	tipsy
association:	member
edited:	false
status:	none
--
Thanks @grzegorzbor, this is frustrating... We had a similar issue earlier, and we supposedly fixed it: https://github.com/javalin/javalin/issues/2117

I guess we have to replace the import here too.
--
author:	tipsy
association:	member
edited:	false
status:	none
--
Apparently there is a fix in Kotlin 1.9.23: https://youtrack.jetbrains.com/issue/KT-66044/JDKs-new-API-is-used-over-Kotlins-SDK-functions#focus=Comments-27-9324700.0-0
--
author:	grzegorzbor
association:	contributor
edited:	true
status:	none
--
We tried upgrading dependency to Kotlin 1.9.23 but it didn't help. 
I think maybe this would help at the build time (i mean Javalin build). But now when javalin 5.6.4 is built and linked to the JDK21 method, there is no way to fix it - the 5.6.4 version is just unusable on JDK < 21
--
author:	tipsy
association:	member
edited:	false
status:	none
--
> I think maybe this would help at the build time (i mean Javalin build). But now when javalin 5.6.4 is built and linked to the JDK21 method, there is no way to fix it - the 5.6.4 version is just unusable on JDK < 21

Yes, I meant that I will try to release using Kotlin 1.9.23 :)
--
author:	tipsy
association:	member
edited:	true
status:	none
--
> Yes, I meant that I will try to release using Kotlin 1.9.23 :)

~We're already on 1.9.23.~ _(Nevermind, I was looking at 6x)_

I will build using JDK 11.
--
author:	tipsy
association:	member
edited:	false
status:	none
--
After spending way too much time guarding against this on the wrong branch (🤦), I have released 5.6.5, built with JDK 11.
--
author:	grzegorzbor
association:	contributor
edited:	false
status:	none
--
Yep works! thx
--
