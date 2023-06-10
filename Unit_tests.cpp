#include <gtest/gtest.h>
#include <sqlite3.h>

class DatabaseTest : public ::testing::Test {
protected:
    virtual void SetUp() {
       
        int rc = sqlite3_open(":memory:", &db);
        if (rc != SQLITE_OK) {

            FAIL() << "Failed to open the database";
        }

        const char* createTableQuery = "CREATE TABLE IF NOT EXISTS sip_packets ("
                                       "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                       "source TEXT,"
                                       "destination TEXT,"
                                       "call_id TEXT)";
        rc = sqlite3_exec(db, createTableQuery, 0, 0, 0);
        if (rc != SQLITE_OK) {
            FAIL() << "Failed to create the database table";
        }
    }

    virtual void TearDown() {
        sqlite3_close(db);
    }

    sqlite3* db;
};

TEST_F(DatabaseTest, QueryTest) {
    const char* query = "SELECT * FROM sip_packets";
    int rc = sqlite3_exec(db, query, 0, 0, 0);

    ASSERT_EQ(rc, SQLITE_OK);
}

int main(int argc, char** argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

